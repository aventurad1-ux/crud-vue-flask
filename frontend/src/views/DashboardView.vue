<template>
  <section>
    <h2>Dashboard</h2>

    <p>
      Bienvenido al sistema de ventas.
      Desde este panel puedes administrar clientes,
      productos y pedidos.
    </p>

    <div class="dashboard-grid">
      <article class="card">
        <h3>Clientes</h3>
        <p>
          Registra, consulta, actualiza y elimina clientes.
        </p>

        <RouterLink to="/clientes">
          Ir a clientes
        </RouterLink>
      </article>

      <article class="card">
        <h3>Productos</h3>
        <p>
          Gestiona productos, precios, stock y estado.
        </p>

        <RouterLink to="/productos">
          Ir a productos
        </RouterLink>
      </article>

      <article class="card">
        <h3>Pedidos</h3>
        <p>
          Crea pedidos y administra su estado.
        </p>

        <RouterLink to="/pedidos">
          Ir a pedidos
        </RouterLink>
      </article>
    </div>
  </section>
</template>