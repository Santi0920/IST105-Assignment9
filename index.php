<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruta con OpenRouteService</title>
</head>
<body>
    <h2>Ingrese la Ubicación de Origen y Destino</h2>
    <form action="process.php" method="post">
        <label for="orig">Ubicación de Origen:</label>
        <input type="text" id="orig" name="orig" required>
        <br><br>
        <label for="dest">Ubicación de Destino:</label>
        <input type="text" id="dest" name="dest" required>
        <br><br>
        <button type="submit">Calcular Ruta</button>
    </form>
</body>
</html>
