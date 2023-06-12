<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">CodeCarreira</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.name == 'home' }" aria-current="page" :to="{ name: 'home' }">Remote</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.name == 'settings' }" :to="{ name: 'settings' }">Settings</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :class="{ active: $route.name == 'buy.coffe' }" :to="{ name: 'buy.coffe' }">Buy me a coffe</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "HeaderComponent",
  methods: {
    toggleNav() {
      document.getElementById("toggleMenu").click();
    },
  },
};
</script>

<style></style>
