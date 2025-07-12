<!DOCTYPE html>
<html>
	<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

		<title> Daftar Absensi Guru SMK NEGERI 1 PEMATANG JAYA</title>
<head>

<body>
	<h2>Daftar Absensi Guru </h2>
	<h1>SMK NEGERI 1 PEMATANG JAYA</h1>
<table border="1" class="table table-dark table-striped">
	<thead>
		<tr>
			<th>id</th>
			<th>Nama</th>
			<th>Tanggal</th>
			<th>Jam</th>
			
		</tr>
	</thead>
	
	<tbody>
	<?php
	
	include ("koneksi.php");
	
	$s="select * from_absensi_guru";
	$q=mysqli_query($k,$s);
	while($r=mysqli_fetch_array($q)){
		print "<tr>";
			print "<td>".$r['id']."</td>";
			print "<td>".$r['nama']."</td>";
			print "<td>".$r['tanggal']."</td>";
			print "<td>".$r['jam']."</td>";
			print "<td><a href='form_edit.php?nama=".$r['nama']."'class='btn btn-primary btn-sm'>EDIT</a> | ";
			print "<a href='hapus.php?noktp=".$r['noktp']."'class='btn btn-danger btn-sm'>HAPUS</a></td>";
		  print"</tr>"; 
	}
		?>
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
	</tbody>
	
</table>