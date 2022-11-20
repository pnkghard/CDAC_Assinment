
<?php
    // Principle : <principle amt>
    // Rate of interest : <rate>
    // Term <number of years>
    // Interest: <calculated interest>
    // Amount: <Toal amount received after term is over>
    $p = $_GET['amt'];
    $r = $_GET['rate'];
    $t = $_GET['time'];
    $int = (($p*$r)/100)*$t;
    $amount = $int + $p;
    echo "Principle : $p <br>";
    echo "Rate of Interest : $r <br>";
    echo "Number of Years : $t <br>";
    echo "Total Interest : $int <br>";
    echo "Net Amount to be paid : $amount";     
?>