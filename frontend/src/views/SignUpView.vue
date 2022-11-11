<template>
    <div id="login">
        <h1>Rejestracja</h1>
      <br />
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="email" name="email" v-model="input.email" placeholder="E-mail" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <input type="password" name="confpassword" v-model="input.confpassword" placeholder="Confirm Password" />
       <br /> <button type="button" v-on:click="signup()">Zarejestuj się</button> <br />
    </div>
</template>
<script>
    export default {
        name: "SignUpView",
        data() {
            return {
                input: {
                    username: "",
                    email: "",
                    password: "",
                    confpassword: ""
               }
           }
        },
    methods: {
            signup() {
                if(this.input.username !== "" && this.input.username !== "" && this.input.password !== "" && this.input.confpassword !== "") {
                    if(this.input.password === this.input.confpassword) {
                        //add to database
                        this.$router.replace({ name: "login" });
                    } else {
                        console.log("Passwords don't match");
                    }
                } else {
                    console.log("All fields must be present");
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