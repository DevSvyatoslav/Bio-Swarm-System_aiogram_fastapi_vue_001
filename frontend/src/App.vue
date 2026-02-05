<script setup lang="ts">
import { onMounted, ref } from 'vue'
import AgentRegistration from './components/AgentRegistration.vue'

// status state
const sysStatus = ref('CONNECTING...')
const vHash = 'SU5USiB8IGRZdlN2eWF0b3NsYXYgfCBCaW9Td2FybQ==' // build version

const checkHealth = async () => {
  try {
    const res = await fetch('http://127.0.0.1:8001/system/health')
    const data = await res.json()
    sysStatus.value = `ONLINE: ${data.status}`
  } catch {
    sysStatus.value = 'ERR: DISCONNECTED'
  }
}

onMounted(() => {
  checkHealth()
})
</script>

<template>
  <div class="min-h-screen bg-black flex flex-col items-center justify-center p-4">
    
    <!-- Header -->
    <div class="mb-8 text-center">
      <h1 class="text-4xl font-bold text-emerald-500 font-mono tracking-widest">
        BIO_SWARM
      </h1>
      <p class="text-xs text-gray-500 font-mono mt-2">
        [{{ sysStatus }}]
      </p>
    </div>

    <!-- Main Component -->
    <AgentRegistration />

    <!-- Footer  -->
    <div class="mt-16 text-gray-800 font-mono text-[10px]">
      v1.0-{{ vHash.slice(0, 10) }}...
    </div>
    
  </div>
</template>