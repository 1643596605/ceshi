<?php
header("Content-Type:text/html;charset = utf-8");
$servername = "localhost";
$username = "root";
$password = "2004523";
$dbname = "kkko";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$object = $_POST['object'];
echo $object;
$describ = $_POST['describe'];
echo $describ;
$contact = $_POST['contact'];
echo $contact;

if(empty($object))
{
    exit;
}
if(empty($describ))
{
    exit;
}
if(empty($contact))
{
    exit;
}
$sql = "INSERT INTO finder (object, describ, contect) VALUES ('$object','$describ','$contact')";
if ($conn->query($sql) === TRUE) {
    echo "新纪录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


mysqli_close($conn);

?>
