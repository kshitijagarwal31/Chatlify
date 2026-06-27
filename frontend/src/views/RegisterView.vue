<template>
  <div class="page">

    <h2 class="app-name">💬 Chatlify</h2>

    <p class="success-msg" v-if="successMessage">{{ successMessage }}</p>
    <p class="error-msg" v-if="errorMessage">{{ errorMessage }}</p>

    <div class="card">

      <h1>Create your account</h1>

      <form @submit.prevent="handleRegister">
        <div class="field">
          <label for="name">Name</label>
          <input id="name" type="text" v-model="name" placeholder="Ali Hassan" />
        </div>

        <div class="field">
          <label for="username">Username</label>
          <input id="username" type="text" v-model="username" placeholder="alihassan" />
        </div>

        <div class="field">
          <label for="password">Password</label>
          <input id="password" type="password" v-model="password" placeholder="Min. 8 characters" />
        </div>

        <button type="submit">Create Account</button>
      </form>

      <p class="signin-link">Already have an account? <router-link to="/login">Sign in</router-link></p>

    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
    name: "RegisterView",

    data() {
        return {
            name: "",
            username: "",
            password: "",
            successMessage: "",
            errorMessage: ""
        }
    },

    methods: {
        async handleRegister() {
            try {
                await axios.post("http://localhost:8000/register", {
                    name: this.name,
                    username: this.username,
                    password: this.password
                })
                this.successMessage = "User registered successfully"

                setTimeout(() => {
                    this.$router.push("/login")
                }, 1000)
            } 
            catch (error) {
                this.errorMessage = error.response.data.detail
            }
        }
    }
}

</script>

<style scoped>

.page {
  min-height: 100vh;
  background: #090910;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Segoe UI', sans-serif;
}

.app-name {
  color: #c4b5fd;
  font-size: 22px;
  margin-bottom: 24px;
}

.card {
  background: #13131f;
  border: 1px solid #2a2a40;
  border-radius: 16px;
  padding: 36px 32px;
  width: 100%;
  max-width: 400px;
}

.card h1 {
  color: #ffffff;
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 24px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

label {
  font-size: 13px;
  color: #9090b0;
}

input {
  background: #0e0e1a;
  border: 1px solid #2a2a42;
  border-radius: 8px;
  padding: 11px 14px;
  font-size: 14px;
  color: #ffffff;
  outline: none;
}

input::placeholder {
  color: #50507a;
}

input:focus {
  border-color: #7c3aed;
}

button {
  width: 100%;
  padding: 12px;
  background: #7c3aed;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 4px;
}

button:hover {
  background: #6d28d9;
}

.signin-link {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #7070a0;
}

.signin-link a {
  color: #a78bfa;
  text-decoration: none;
}

.signin-link a:hover {
  text-decoration: underline;
}

.success-msg {
    color: #22c55e;
    text-align: center;
    font-size: 14px;
    margin-top: 10px;
}

.error-msg {
    color: #ef4444;
    text-align: center;
    font-size: 14px;
    margin-top: 10px;
}

</style>