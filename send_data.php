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
        $bags=array("cabin"=>6000, "sack"=>2000, "handbag"=>3000);
        $shoes=array("walking"=>4000, "trekking"=>10000);
        $cloths=array("Tshirt"=>3000, "tops"=>4567, "jeans"=>5000);
        session_start();
        $cat=$_REQUEST['Category'];
        $price=$_REQUEST['Price'];
        $btn=$_REQUEST['btn'];
        if($cat=="bags"){
            foreach($bags as $bag=>$pr){
                if($pr>=$price){
                    echo "$bag-->$pr <br>";
                }
            }            
        } elseif($cat=="shoes"){
            foreach($shoes as $sh=>$pr){
                if($pr>=$price){
                    echo "$sh-->$pr <br>";
                }
            }            
        } elseif($cat=="cloths") {
            foreach($cloths as $cl=>$pr){
                if($pr>=$price){
                    echo "$cl-->$pr <br>";
                }
            }            
        }
        $_SESSION['pro'] = $cat;
        $_SESSION['pry'] = $price;                
    ?>
    <p> <a href="Logout.php">click here to logout session</a> </p>
</body>
</html>