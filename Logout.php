<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
    </style>
</head>
<body>
    <?php
        session_start();
        echo "You seleceted ".$_SESSION['pro']." and price ".$_SESSION['pry'];
        echo "<br> visit again..";
        session_unset();
        session_destroy();
    ?>    
</body>
</html>