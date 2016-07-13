
function clickInfoComputePrediction(){

if ($('#info_compute_prediction_btn').val()=="See Manual"){
$('.info_compute_prediction').css({'display':'block'});
$('#info_compute_prediction_btn').val('Hide');
}

else {
$('.info_compute_prediction').css({'display':'none'});
$('#info_compute_prediction_btn').val('See Manual');

}
}



function clickInfoMutate(){

if ($('#info_mutate_btn').val()=="See Manual"){
$('.info_mutate').css({'display':'block'});
$('#info_mutate_btn').val('Hide');
}

else {
$('.info_mutate').css({'display':'none'});
$('#info_mutate_btn').val('See Manual');

}
}
