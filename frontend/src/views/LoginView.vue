<template>
  <div class="page">

    <h2 class="app-name">💬 Chatlify</h2>

    <p class="error-msg" v-if="errorMessage">{{ errorMessage }}</p>

    <div class="card">

      <h1>Welcome back</h1>

      <form @submit.prevent="handleLogin">
        <div class="field">
          <label for="username">Username</label>
          <input id="username" type="text" v-model="username" placeholder="alihassan" />
        </div>

        <div class="field">
          <label for="password">Password</label>
          <input id="password" type="password" v-model="password" placeholder="Enter your password" />
        </div>

        <button type="submit">Sign In</button>
      </form>

      <p class="register-link">Don't have an account? <router-link to="/">Create one</router-link></p>

    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
    name: "LoginView",

    data() {
        return {
            username: "",
            password: "",
            errorMessage: ""
        }
    },

    methods: {
        async handleLogin() {
            try {
                this.errorMessage = ""

                const response = await axios.post("http://localhost:8000/login", {
                    username: this.username,
                    password: this.password
                })
                
                localStorage.setItem("token", response.data.access_token)
                localStorage.setItem("user_id", response.data.user_id)

                this.$router.push("/chat")

            } 
            catch (error) {
                if (error.response) {
                    this.errorMessage = error.response.data.detail
                } else {
                    this.errorMessage = "Something went wrong!"
                }
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

.register-link {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #7070a0;
}

.register-link a {
  color: #a78bfa;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}

.error-msg {
    color: #ef4444;
    text-align: center;
    font-size: 14px;
    margin-top: 10px;
}

</style>