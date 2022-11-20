<!-- 2.  Design a form to accept username and password from user,
    Check whether user is valid or not
    Usernames are stored in uname array.
    If user found display message “valid user” otherwise display message “invalid user”. -->

<?php
    $uname=array("username"=>"password", "pankaj"=>"gharde");
    $name=$_POST['name'];    
    $passwd=$_POST['passwd'];
    $flag=false;
    foreach($uname as $k=>$v) {
        if($name==$k){
            if($passwd==$v) {
                echo "Valid User....";
                $flag=true;
                break;
            }
        }
    }
    if(!$flag) {
        echo "Wrong username or password enter...";
    }    
?>