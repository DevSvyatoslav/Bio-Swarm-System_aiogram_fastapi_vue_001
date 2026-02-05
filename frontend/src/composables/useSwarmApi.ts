// frontend/src/composables/useSwarmApi.ts
import { ref } from 'vue'

export function useSwarmApi() {
  const isLoading = ref(false)
  const error = ref<string | null>(null)
  
  // Базовый URL твоего бэкенда
  const BASE_URL = 'http://127.0.0.1:8001/api/v1'

  // Функция вербовки (Регистрации)
  const recruitAgent = async (agentData: any) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${BASE_URL}/users/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(agentData)
      })

      if (!response.ok) {
        const errData = await response.json()
        throw new Error(errData.detail || 'Ошибка вербовки')
      }

      return await response.json() // Возвращаем созданного агента
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  return {
    recruitAgent,
    isLoading,
    error
  }
}