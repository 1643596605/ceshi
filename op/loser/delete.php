<?php

$servername = "localhost";
$username = "root";
$password = "2004523";
$dbname = "kkko";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "SUCCESS\n";


$deleteone = $_POST['deleteone'];
$sql = "DELETE FROM giver WHERE id = $deleteone";
mysqli_query($conn,$sql);

$sql = "alter table giver drop id";
mysqli_query($conn,$sql);
$sql = "alter table giver add id bigint primary key not null auto_increment first";
mysqli_query($conn,$sql);
echo "SUCCESS";
echo "SUCCESS";

$conn->close();

?>



