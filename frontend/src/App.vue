<template>
  <div class="app-container">
    <SignIn />
  </div>
</template>

<script>
import SignIn from "./components/SignIn.vue";

export default {
  name: "App",
  components: {
    SignIn,
  },
};
</script>