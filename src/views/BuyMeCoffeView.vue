<template>
  <div class="container">
    <div class="row mt-3">
      <div class="col">
        <h1>Buy me a Coffe</h1>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">BTC</span>
              <input
                type="text"
                class="form-control"
                aria-label="BTC-WALLET"
                aria-describedby="btc-wallet"
                value="bc1qzwajr83pmrre07a5xas0j8cgsf4vt907u5zddz"
                disabled
              />
              <button class="btn btn-outline-secondary" type="button btn-dark" @click="copyText('bc1qzwajr83pmrre07a5xas0j8cgsf4vt907u5zddz')">Copy</button>
            </div>
          </div>
          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">DASH</span>
              <input
                type="text"
                class="form-control"
                aria-label="DASH-WALLET"
                aria-describedby="btc-wallet"
                value="XhBdfys8FUsRUj3gv33UpbCQ4aHt3iNxzq"
                disabled
              />
              <button class="btn btn-outline-secondary" type="button btn-dark" @click="copyText('XhBdfys8FUsRUj3gv33UpbCQ4aHt3iNxzq')">Copy</button>
            </div>
          </div>
          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">ETH</span>
              <input
                type="text"
                class="form-control"
                aria-label="ETH-WALLET"
                aria-describedby="eth-wallet"
                value="0xD60289664172dCFb43b7025DC3C86e28075fC71F"
                disabled
              />
              <button class="btn btn-outline-secondary" type="button btn-dark" @click="copyText('0xD60289664172dCFb43b7025DC3C86e28075fC71F')">Copy</button>
            </div>
          </div>

          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">Litecoin</span>
              <input
                type="text"
                class="form-control"
                aria-label="LTC-WALLET"
                aria-describedby="ltc-wallet"
                value="LeVztvy6YU5YCyYJNVHZYj7QyQ6FQCLJHF"
                disabled
              />
              <button class="btn btn-outline-secondary" type="button btn-dark" @click="copyText('LeVztvy6YU5YCyYJNVHZYj7QyQ6FQCLJHF')">Copy</button>
            </div>
          </div>
          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">Monero</span>
              <input
                type="text"
                class="form-control"
                aria-label="XMR-WALLET"
                aria-describedby="xmr-wallet"
                value="46k1pbJisemRwpvW5fhLnZEw4X4NSMSJjHAWN7ouRCmuhvRzkmi9Ln29ToBYaeKUbLFmdz1P9NXnKGS3th2Wm28nD67PCGS"
                disabled
              />
              <button
                class="btn btn-outline-secondary"
                type="button btn-dark"
                @click="copyText('46k1pbJisemRwpvW5fhLnZEw4X4NSMSJjHAWN7ouRCmuhvRzkmi9Ln29ToBYaeKUbLFmdz1P9NXnKGS3th2Wm28nD67PCGS')"
              >
                Copy
              </button>
            </div>
          </div>
        </div>
        <div class="row" v-if="showAlert">
          <div class="col">
            <div class="alert alert-success" id="copyAlert" role="alert">Wallet successfully copied to clipboard!</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Clipboard } from "@capacitor/clipboard";
export default {
  name: "BuyMeCoffeView",
  data() {
    return {
      showAlert: false,
      alertTimeout: null,
    };
  },
  methods: {
    async copyText(text) {
      await Clipboard.write({
        string: text,
      });
      this.showAlert = true;
    },
  },
  watch: {
    showAlert(val) {
      if (val) {
        if (this.alertTimeout) {
          clearInterval(this.alertTimeout);
        }
        this.alertTimeout = setTimeout(() => {
          this.showAlert = false;
        }, 5000);
      }
    },
  },
};
</script>

<style></style>
