<?php
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
$address = $_POST['position'];
echo $address;
$contect = $_POST['contact'];
echo $contect;
if(empty($object))
{
    exit;
}
if(empty($address))
{
    exit;
}
if(empty($contect))
{
    exit;
}
$file = $_FILES['upload_image'];
$fileName = $_FILES['upload_image']['name'];
$fileTempName = $_FILES['upload_image']['tmp_name'];
$fileEXt = explode('.', $fileName);
$fileActualExt = strtolower(end($fileEXt));

$fileNameNew = uniqid('',true).".".$fileActualExt;
$fileDestination ='images/'.$fileNameNew;
move_uploaded_file($fileTempName,$fileDestination);

$sql = "INSERT INTO giver (object, address, contect, upload_image) VALUES ('$object','$address', '$contect','$fileDestination')";
if ($conn->query($sql) === TRUE) {
    echo "新纪录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


mysqli_close($conn);

?>
