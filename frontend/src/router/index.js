import { createRouter, createWebHistory } from "vue-router"


import RegisterView from "../views/RegisterView.vue"
import LoginView from "../views/LoginView.vue"
import ChatView from "../views/ChatView.vue"


const routes = [
    {path: "/", component: RegisterView},
    {path: "/login", component: LoginView},
    {path: "/chat", component: ChatView}
]



const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem("token")
    
    if (to.path === "/chat" && !token) {
        next("/login")
    } else {
        next()
    }
})


export default router