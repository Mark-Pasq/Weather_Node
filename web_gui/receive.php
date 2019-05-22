<?php
include("global.php");
if (isset($_REQUEST["data"])){
	$db = new MyDB();
	$data_raw_in = json_decode($_REQUEST["data"]);
	$jsonarray = array();
	foreach ($data_raw_in as $k => $v){
		array_push($jsonarray, $k);
		$real_timestamp = str_replace("]", "", str_replace("[", "", explode("[data]", $v)[0]));
		$real_data = str_replace("[/data]", '', explode("[data]", $v)[1]);
		insert_record($db, $real_timestamp, $real_data);
	}
	echo json_encode($jsonarray);
}else{
	echo "internal error";
}
?>
