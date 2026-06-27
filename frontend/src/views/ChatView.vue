<template>
  <div class="page">

    <div class="navbar">
      <h2 class="app-name">💬 Chatlify</h2>
      <div class="nav-right">
        <span class="room-name"># general</span>
        <button class="logout-btn" @click="logout">Logout</button>
      </div>
    </div>

    <div class="messages-area">

      <div class="message" v-for="(msg, index) in messages" :key="index">
        <div class="avatar">{{ msg[0] }}</div>
        <div class="msg-content">
          <span class="msg-username">{{ msg }}</span>
          <span class="msg-time">{{ new Date().toLocaleTimeString() }}</span>
        </div>
      </div>

    </div>

    <div class="input-area">
      <input type="text" v-model="newMessage" class="msg-input" placeholder="Type a message..." />
      <button class="send-btn" @click="sendMessage">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <line x1="22" y1="2" x2="11" y2="13" stroke="white" stroke-width="2" stroke-linecap="round"/>
          <polygon points="22 2 15 22 11 13 2 9 22 2" stroke="white" stroke-width="2" stroke-linejoin="round" fill="none"/>
        </svg>
      </button>
    </div>

  </div>
</template>

<script>
import axios from "axios"

export default {
    name: "ChatView",

    data() {
        return {
            messages: [],
            newMessage: "",
            socket: null
        }
    },

    mounted() {
        const user_id = localStorage.getItem("user_id")
        this.socket = new WebSocket(`ws://localhost:8000/ws/${user_id}`)

        this.socket.onmessage = (event) => {
            this.messages.push(event.data)
        }
    },

    beforeUnmount() {
        this.socket.close()
    },

    methods: {
        async sendMessage() {
            if (!this.newMessage.trim()) return 

            const token = localStorage.getItem("token")

            await axios.post("http://localhost:8000/message",
                {content: this.newMessage},
                {headers: {Authorization: `Bearer ${token}`}}
            )

            this.newMessage = ""
        },

        logout() {
            localStorage.removeItem("token")
            localStorage.removeItem("user_id")
            this.$router.push("/login")
        }
    }
}
</script>

<style scoped>

.page {
  height: 100vh;
  background: #090910;
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', sans-serif;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 24px;
  background: #13131f;
  border-bottom: 1px solid #2a2a40;
}

.app-name {
  color: #c4b5fd;
  font-size: 20px;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.room-name {
  color: #9090b0;
  font-size: 14px;
  font-weight: 600;
}

.logout-btn {
  background: transparent;
  border: 1px solid #2a2a40;
  color: #9090b0;
  padding: 7px 16px;
  border-radius: 8px;
  font-size: 13px;
  cursor: pointer;
}

.logout-btn:hover {
  border-color: #7c3aed;
  color: #c4b5fd;
}

.messages-area {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.message {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.avatar {
  width: 38px;
  height: 38px;
  background: #7c3aed;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 700;
  font-size: 15px;
  flex-shrink: 0;
}

.msg-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.msg-username {
  color: #c4b5fd;
  font-size: 14px;
  font-weight: 600;
}

.msg-time {
  color: #50507a;
  font-size: 11px;
  margin-left: 8px;
}

.msg-text {
  color: #d0d0f0;
  font-size: 14px;
  line-height: 1.5;
}

.input-area {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 24px;
  background: #13131f;
  border-top: 1px solid #2a2a40;
}

.msg-input {
  flex: 1;
  background: #0e0e1a;
  border: 1px solid #2a2a42;
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 14px;
  color: #ffffff;
  outline: none;
}

.msg-input::placeholder {
  color: #50507a;
}

.msg-input:focus {
  border-color: #7c3aed;
}

.send-btn {
  width: 44px;
  height: 44px;
  background: #7c3aed;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.send-btn:hover {
  background: #6d28d9;
}

</style>