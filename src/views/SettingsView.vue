<template>
  <div class="container">
    <div class="row mt-3">
      <div class="col">
        <h1>Settings</h1>
      </div>
      <div class="container">
        <div class="row">
          <div class="col"></div>
          <div class="col-8">
            <form @submit.prevent="save">
              <div class="mb-3">
                <label for="ipAddress" class="form-label">IP</label>
                <input type="text" class="form-control" id="ipAddress" aria-describedby="info-ip" v-model="config.ip" />
                <div id="info-ip" class="form-text">Ex: 192.168.0.1</div>
              </div>
              <div class="mb-3">
                <label for="ipAddress" class="form-label">PORT</label>
                <input type="text" class="form-control" id="ipAddress" aria-describedby="info-ip" v-model="config.port" />
                <div id="info-ip" class="form-text">Ex: 8085</div>
              </div>

              <button type="submit" class="btn btn-primary">Save</button>
            </form>
          </div>
          <div class="col"></div>
        </div>
        <div class="row mt-2">
          <div class="col"></div>
          <div class="col-8">
            <div class="alert alert-success" role="alert" v-if="result.show && !result.danger">{{ result.message }}</div>
            <div class="alert alert-danger" role="alert" v-if="result.show && result.danger">{{ result.message }}</div>
          </div>

          <div class="col"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsView",
  data() {
    return {
      config: {
        ip: "",
        port: "",
      },
      result: {
        message: "",
        danger: false,
        show: false,
      },
      timer: null,
    };
  },
  methods: {
    save() {
      clearInterval(this.timer);

      try {
        localStorage.setItem("ip", this.config.ip);
        localStorage.setItem("port", this.config.port);
        this.result.message = "Settings updated!";
        this.result.show = true;
        this.timer = setTimeout(() => {
          this.result.show = false;
        }, 5000);
      } catch (e) {
        this.result.show = true;
        this.result.danger = true;
        this.result.message = `Error updating settings! ${JSON.stringify(e)}`;
        this.timer = setTimeout(() => {
          this.result.show = false;
        }, 5000);
      }
    },
  },
  mounted() {
    this.config.ip = localStorage.getItem("ip");
    this.config.port = localStorage.getItem("port");
  },
};
</script>

<style></style>
