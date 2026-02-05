<!-- frontend/src/components/AgentRegistration.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useSwarmApi } from '../composables/useSwarmApi'

const { recruitAgent, isLoading, error } = useSwarmApi()

// Данные формы
const form = ref({
  email: '',
  username: '',
  password: ''
})

const successMessage = ref('')

const handleSubmit = async () => {
  successMessage.value = ''
  try {
    // Отправляем данные в "Мозг"
    await recruitAgent(form.value)
    successMessage.value = `Агент ${form.value.username} успешно интегрирован в Рой.`
    // Очищаем форму
    form.value = { email: '', username: '', password: '' }
  } catch (e) {
    // Ошибка уже обработана в composable, она появится в переменной error
    console.error(e)
  }
}
</script>

<template>
  <div class="bg-gray-800 p-8 rounded-lg border border-emerald-500/30 shadow-2xl max-w-md w-full">
    <h2 class="text-2xl font-bold text-emerald-400 mb-6 font-mono border-b border-emerald-500/30 pb-2">
      > NEW AGENT PROTOCOL
    </h2>

    <form @submit.prevent="handleSubmit" class="space-y-4">
      
      <!-- Username -->
      <div>
        <label class="block text-emerald-500/70 text-sm font-mono mb-1">CODENAME (Username)</label>
        <input 
          v-model="form.username" 
          type="text" 
          class="w-full bg-gray-900 border border-emerald-500/30 text-emerald-100 p-2 rounded focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all font-mono"
          placeholder="Neo_v1"
        />
      </div>

      <!-- Email -->
      <div>
        <label class="block text-emerald-500/70 text-sm font-mono mb-1">COMM_LINK (Email)</label>
        <input 
          v-model="form.email" 
          type="email" 
          required
          class="w-full bg-gray-900 border border-emerald-500/30 text-emerald-100 p-2 rounded focus:outline-none focus:border-emerald-500 font-mono"
          placeholder="neo@matrix.net"
        />
      </div>

      <!-- Password -->
      <div>
        <label class="block text-emerald-500/70 text-sm font-mono mb-1">ACCESS_KEY (Password)</label>
        <input 
          v-model="form.password" 
          type="password" 
          required
          class="w-full bg-gray-900 border border-emerald-500/30 text-emerald-100 p-2 rounded focus:outline-none focus:border-emerald-500 font-mono"
          placeholder="********"
        />
      </div>

      <!-- Status Messages -->
      <div v-if="error" class="p-3 bg-red-900/30 border border-red-500 text-red-400 text-sm font-mono">
        [ERROR]: {{ error }}
      </div>
      
      <div v-if="successMessage" class="p-3 bg-emerald-900/30 border border-emerald-500 text-emerald-400 text-sm font-mono">
        [SUCCESS]: {{ successMessage }}
      </div>

      <!-- Submit Button -->
      <button 
        type="submit" 
        :disabled="isLoading"
        class="w-full bg-emerald-600 hover:bg-emerald-500 text-black font-bold py-2 px-4 rounded font-mono transition-colors disabled:opacity-50 disabled:cursor-not-allowed mt-4"
      >
        <span v-if="isLoading">UPLOADING DNA...</span>
        <span v-else>INITIALIZE AGENT</span>
      </button>

    </form>
  </div>
</template>