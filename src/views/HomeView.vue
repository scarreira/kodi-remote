<template>
  <div class="container">
    <div class="row mt-3">
      <div class="col">
        <button type="button" class="btn btn-primary" @click="volume(false)"><i class="bi bi-volume-down"></i></button>
        <button type="button" class="btn btn-danger mx-3" @click="shutdown()"><i class="bi bi-power"></i></button>
        <button type="button" class="btn btn-primary" @click="volume(true)"><i class="bi bi-volume-up"></i></button>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col"></div>
      <div class="col">
        <button type="button" class="btn btn-primary" @click="channel(true)" style="width: 50px"><i class="bi bi-arrow-up"></i></button>
      </div>
      <div class="col"></div>
    </div>
    <div class="row mt-1">
      <div class="col"></div>
      <div class="col-8 text-center">
        <button type="button" class="btn btn-primary" @click="move(false)"><i class="bi bi-arrow-left"></i></button>
        <button type="button" class="btn btn-secondary mx-1" @click="action('ok')">OK</button>
        <button type="button" class="btn btn-primary" @click="move(true)">
          <i class="bi bi-arrow-right"></i>
        </button>
      </div>
      <div class="col"></div>
    </div>
    <div class="row mt-1">
      <div class="col"></div>
      <div class="col-8">
        <button type="button" class="btn btn-warning" @click="setMute(false)"><i class="bi bi-volume-up-fill"></i></button>
        <button type="button" class="btn btn-primary mx-1" @click="channel(false)" style="width: 50px"><i class="bi bi-arrow-down"></i></button>
        <button type="button" class="btn btn-warning" @click="setMute(true)"><i class="bi bi-volume-mute-fill"></i></button>
      </div>
      <div class="col"></div>
    </div>

    <div class="btn-group-vertical ml-4 mt-4" role="group" aria-label="Numpad">
      <div class="row">
        <div class="btn-group">
          <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(1)">1</button>
          <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(2)">2</button>
          <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(3)">3</button>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <div class="btn-group">
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(4)">4</button>
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(5)">5</button>
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(6)">6</button>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <div class="btn-group">
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(7)">7</button>
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(8)">8</button>
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(9)">9</button>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <div class="btn-group">
            <button type="button" class="btn btn-outline-secondary py-3 p-5" style="max-width: 107px" @click="action('back')">
              <i class="bi bi-arrow-return-left"></i>
            </button>
            <button type="button" class="btn btn-outline-secondary py-3 p-5" @click="changeChannel(0)">0</button>
            <button type="button" class="btn btn-primary py-3 p-5" style="max-width: 108px" @click="action('ok')">OK</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import Swal from "sweetalert2";
//import jsonp from "jsonp";

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      host: "http://192.168.10.68:8085/api/v1",
      mute: false,
    };
  },
  methods: {
    async changeChannel(channel) {
      console.log(channel);
      // Expects localhost and port 9090.

      await axios
        .get(`${this.host}/change-channel?ch=${channel}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
    async setMute(val) {
      await axios
        .get(`${this.host}/mute?mute=${val}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
    async volume(up) {
      let route = up ? "volume-up" : "volume-down";
      await axios
        .get(`${this.host}/${route}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch((e) => {
          console.log(e);
        })
        .finally(() => {});
    },
    async channel(up) {
      let route = up ? "channel-up" : "channel-down";

      await axios
        .get(`${this.host}/${route}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
    async move(right) {
      let route = right ? "right" : "left";

      await axios
        .get(`${this.host}/${route}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
    async action(action) {
      let route = action == "ok" ? "ok" : "back";

      await axios
        .get(`${this.host}/${route}`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
    async shutdown() {
      Swal.fire({
        title: "Confirm shutdown?",
        showDenyButton: true,
        confirmButtonColor: "#dc3545",
        denyButtonColor: "#6c757d",
        confirmButtonText: "Yes",
        denyButtonText: `No`,
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          this.shutdownConfirmed();
        } else if (result.isDenied) {
          return;
        }
      });
    },
    async shutdownConfirmed() {
      await axios
        .get(`${this.host}/shutdown`)
        .then(({ data }) => {
          console.log(data);
        })
        .catch(({ data }) => {
          console.log(data);
        })
        .finally(() => {});
    },
  },
  mounted() {
    const ip = localStorage.getItem("ip");
    const port = localStorage.getItem("port");

    if (ip && port) {
      this.host = `http://${ip}:${port}/api/v1`;
    } else {
      localStorage.setItem("ip", "192.168.10.68");
      localStorage.setItem("port", "8085");
    }
  },
};
</script>
