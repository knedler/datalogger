<?php
# File taken from Sheaff modified for single data set
header('Content-Type: text/json');

$data['ip'] = getHostByName(getHostName());
$data['ip'] = $_SERVER['HTTP_HOST'];
$db = new SQLite3('data.db');

# Data passed from the client for panning
$min = (int)($_POST['min']);
if (empty($min)) {
    $min = 0;
}

$max = (int)($_POST['max']);
if (empty($max)) {
    $max = 0;
}

# Calculate the start and stop times
if (($min == 0) || ($max == 0)) {
    $d = new DateTime();
    $j = new DateInterval('P1D');
    $max = $d->getTimestamp();
    $min = $d->sub($j)->getTimestamp();
}

$dtmax = new DateTime("@$max");
$dtmin = new DateTime("@$min");
$maxs = $dtmax->format('Y-m-d\TH:i:s0');
$mins = $dtmin->format('Y-m-d\TH:i:s0');
$statement = $db->prepare("select DateTime as datetime, Temp as mw_temp from temperature where datetime <= ? and datetime >= ?");
$statement->bindValue(1, $maxs, SQLITE3_TEXT);
$statement->bindValue(2, $mins, SQLITE3_TEXT);
$result = $statement->execute();
$i = 0;
while ($res = $result->fetchArray(SQLITE3_ASSOC)) {
    $dt = $res['datetime'];
    $data['mw_temp'][$i]['x'] = $dt;
    $data['mw_temp'][$i]['y'] = ($res['mw_temp'] * 9/5) - 459.67;
    $i++;
}
$db->close();

echo json_encode($data);
?>

