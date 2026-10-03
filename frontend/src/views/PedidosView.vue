<template>
  <section>
    <h2>Pedidos</h2>

    <AlertMessage :message="error" />

    <form
      class="card form-grid"
      @submit.prevent="crearPedido"
    >
      <label class="field">
        <span>Cliente</span>

        <select
          v-model.number="form.cliente_id"
          required
        >
          <option
            disabled
            value=""
          >
            Seleccione un cliente
          </option>

          <option
            v-for="cliente in clientes"
            :key="cliente.id"
            :value="cliente.id"
          >
            {{ cliente.nombre }}
          </option>
        </select>
      </label>

      <label class="field">
        <span>Producto</span>

        <select
          v-model.number="form.producto_id"
          required
        >
          <option
            disabled
            value=""
          >
            Seleccione un producto
          </option>

          <option
            v-for="producto in productos"
            :key="producto.id"
            :value="producto.id"
          >
            {{ producto.nombre }} — Q{{ producto.precio }}
            — Stock: {{ producto.stock }}
          </option>
        </select>
      </label>

      <BaseInput
        v-model.number="form.cantidad"
        label="Cantidad"
        type="number"
      />

      <div class="form-actions">
        <BaseButton
          type="submit"
          :disabled="guardando"
        >
          Crear pedido
        </BaseButton>
      </div>
    </form>

    <DataTable
      :rows="pedidos"
      :columns="columns"
    >
      <template #actions="{ row }">
        <select
          :value="row.estado"
          @change="cambiarEstado(row, $event.target.value)"
        >
          <option value="pendiente">
            Pendiente
          </option>

          <option value="pagado">
            Pagado
          </option>

          <option value="enviado">
            Enviado
          </option>

          <option value="cancelado">
            Cancelado
          </option>
        </select>

        <BaseButton
          variant="danger"
          @click="eliminar(row)"
        >
          Eliminar
        </BaseButton>
      </template>
    </DataTable>
  </section>
</template>

<script setup>
import {
  onMounted,
  reactive,
  ref,
} from 'vue'

import { clientesApi } from '../api/clientes'
import { pedidosApi } from '../api/pedidos'
import { productosApi } from '../api/productos'

import AlertMessage from '../components/AlertMessage.vue'
import BaseButton from '../components/BaseButton.vue'
import BaseInput from '../components/BaseInput.vue'
import DataTable from '../components/DataTable.vue'

const clientes = ref([])
const productos = ref([])
const pedidos = ref([])

const error = ref('')
const guardando = ref(false)

const columns = [
  {
    key: 'id',
    label: 'ID',
  },
  {
    key: 'cliente',
    label: 'Cliente',
  },
  {
    key: 'producto',
    label: 'Producto',
  },
  {
    key: 'cantidad',
    label: 'Cantidad',
  },
  {
    key: 'estado',
    label: 'Estado',
  },
  {
    key: 'total',
    label: 'Total',
  },
]

const form = reactive({
  cliente_id: '',
  producto_id: '',
  cantidad: 1,
})

function limpiarFormulario() {
  Object.assign(form, {
    cliente_id: '',
    producto_id: '',
    cantidad: 1,
  })
}

async function cargarDatos() {
  error.value = ''

  try {
    const [
      clientesResponse,
      productosResponse,
      pedidosResponse,
    ] = await Promise.all([
      clientesApi.listar(),
      productosApi.listar(),
      pedidosApi.listar(),
    ])

    clientes.value = clientesResponse.data
    productos.value = productosResponse.data
    pedidos.value = pedidosResponse.data

  } catch (err) {
    error.value = err.message
  }
}

async function crearPedido() {
  error.value = ''

  if (!form.cliente_id) {
    error.value = 'Debe seleccionar un cliente'
    return
  }

  if (!form.producto_id) {
    error.value = 'Debe seleccionar un producto'
    return
  }

  if (
    !form.cantidad ||
    Number(form.cantidad) <= 0
  ) {
    error.value =
      'La cantidad debe ser mayor que cero'
    return
  }

  guardando.value = true

  try {
    await pedidosApi.crear({
      cliente_id: form.cliente_id,
      producto_id: form.producto_id,
      cantidad: form.cantidad,
    })

    limpiarFormulario()

    await cargarDatos()

  } catch (err) {
    error.value = err.message

  } finally {
    guardando.value = false
  }
}

async function cambiarEstado(
  pedido,
  nuevoEstado,
) {
  error.value = ''

  try {
    await pedidosApi.actualizar(
      pedido.id,
      {
        estado: nuevoEstado,
      },
    )

    await cargarDatos()

  } catch (err) {
    error.value = err.message
  }
}

async function eliminar(pedido) {
  const confirmar = window.confirm(
    `¿Eliminar el pedido #${pedido.id}?`,
  )

  if (!confirmar) {
    return
  }

  error.value = ''

  try {
    await pedidosApi.eliminar(
      pedido.id,
    )

    await cargarDatos()

  } catch (err) {
    error.value = err.message
  }
}

onMounted(cargarDatos)
</script>