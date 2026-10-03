def test_crear_y_listar_producto(client):
    response = client.post(
        "/api/productos",
        json={
            "nombre": "Producto de prueba",
            "descripcion": "Producto creado desde pytest",
            "precio": 99.99,
            "stock": 5,
            "activo": True,
        },
    )

    assert response.status_code == 201
    assert response.json["nombre"] == "Producto de prueba"
    assert response.json["stock"] == 5

    response = client.get("/api/productos")

    assert response.status_code == 200
    assert len(response.json) == 1