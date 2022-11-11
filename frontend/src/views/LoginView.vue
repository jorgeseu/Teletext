<template>
    <div id="login">
        <h1>Logowanie</h1>
      <br />
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
       <br /> <button type="button" v-on:click="login()">Zaloguj się</button> <br />
    </div>
</template>

<script>
    export default {
        name: 'LoginView',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login() {
                if(this.input.username !== "" && this.input.password !== "") {
                    if(this.input.username === "username" && this.input.password === "password") {
                        this.$emit("authenticated", true);
                        this.$router.replace({ name: "tv" });
                    } else {
                        console.log("The username and / or password is incorrect");
                    }
                } else {
                    console.log("A username and password must be present");
                }
            }
        }
    }
</script>

<style scoped>
  input {
    display: block;
    margin: 10px;
  }

</style>