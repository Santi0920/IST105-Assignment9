<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $orig = escapeshellarg($_POST["orig"]);
    $dest = escapeshellarg($_POST["dest"]);


    $command = "python3 09_openroute_parse_json.py $orig $dest";
    $output = shell_exec($command);

    echo "<h2>Resultado:</h2>";
    echo "<pre>$output</pre>";
} else {
    echo "Método no permitido.";
}
?>
