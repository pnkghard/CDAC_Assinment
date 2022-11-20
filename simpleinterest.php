<!--
    PHP assignment
    Day 1
    1. Design a file simpleinterest.php to display a form , accept principle, rate of interest, number 
    of years from user.
    Once you submit data, send it to file calculateinterest.php, display 
-->

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
    <form action="calculateinterest.php" method="get">
        <h1>Principle Amount : <input type="text" name="amt" id="Amount"></h1>
        <h1>Rate of Interest : <input type="text" name="rate" id="Rate"></h1>
        <h1>Years of Interest : <input type="text" name="time" id="Time"></h1>
        <h1><button type="submit" name="btn" value="interest">Calculate Interest</button></h1>        
    </form>    
</body>
</html>