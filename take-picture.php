<?php

// Brightness is set by the query string in the URL
$brightness = $_GET["br"];

// Execute the Python script to take the picture
$result = exec("sudo /var/www/html/camera/camera.py " . escapeshellarg($brightness));

// Echo the output from Python
echo $result;

?>
