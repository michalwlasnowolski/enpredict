function validation(seq_field, num_outputs, cut_off, k_choice, random_from_best, region, selectedText){


var error_text='';

try {


    if (/[^atgcATGC]/g.test(seq_field)) throw "has wrong characters";

    if (selectedText == "fly") {
        if (seq_field.length != 200) throw "length is " + seq_field.length + " (should be 200 for D. melanogaster classifier)";
    
    }

    if (selectedText == "fantom_heart" | selectedText == "fantom_brain" | selectedText == "fantom_both") {
        if (seq_field.length != 300) throw "length is " + seq_field.length + " (should be 300 for FANTOM classifier)";
    
    }

    if (selectedText == "vista_heart" | selectedText == "vista_neural" | selectedText == "vista_positives") {
        if (seq_field.length != 1500) throw "length is " + seq_field.length + " (should be 1500 for VISTA classifier)";
    
    }

}

catch(err) {

        error_text+='Error: sequence ' + err + '\n'; 
    }

try {


        if(num_outputs == "") throw "not integer";

        
        num_outputs=Number(num_outputs);
        if (!Number.isInteger(num_outputs)) throw "not integer";
        if (num_outputs<1) throw "too small (min. 1)";
}

catch(err) {

        error_text+='Error: max. number of outputs is ' + err + '\n'; 
    }

try {


        if(k_choice == "") throw "not integer";

        
        k_choice=Number(k_choice);
        if (!Number.isInteger(k_choice)) throw "not integer";
        if (k_choice<1) throw "too small (min. 1)";
}

catch(err) {

        error_text+='Error: n best sequences is ' + err + '\n'; 
    }

try {


        if(random_from_best == "") throw "not integer";

        
        random_from_best=Number(random_from_best);
        if (!Number.isInteger(random_from_best)) throw "not integer";
        if (random_from_best<1) throw "too small (min. 0)";
}

catch(err) {

        error_text+='Error: k best sequences is ' + err + '\n'; 
    }


try {


        if(cut_off == "") throw "is not float";

        
        cut_off=Number(cut_off);
        if (cut_off < 0 | cut_off > 1) throw "must be in the range: 0-1";

}

catch(err) {

        error_text+='Error: cut-off ' + err + '\n'; 
    }

try {



        if (region.length != 0){

        if (region.indexOf(':') === -1) throw "has wrong format";

        region_array=region.split(":");

        if (region_array.length > 2) throw "has wrong format";

        if(isNaN(region_array[0]) | isNaN(region_array[1])) throw "elements are not a numbers";
        
        region_array[0]=Number(region_array[0]);
        region_array[1]=Number(region_array[1]);

        if (region_array[1]-region_array[0] <= 0) throw "has wrong range";
        
        if (region_array[1]>seq_field.length) throw "has wrong range";
        
}
}

catch(err) {

        error_text+='Error: region ' + err + '\n'; 
    }



return error_text;

}


function clickSpoil(seq_field, num_outputs, cut_off, k_choice, random_from_best, region, csrf_token) {    


var seq_field=$("#"+seq_field).val();
var num_outputs=$("#"+num_outputs).val();
var cut_off=$("#"+cut_off).val();
var k_choice=$("#"+k_choice).val();
var random_from_best=$("#"+random_from_best).val();
var region=$("#"+region).val();
var selectedText=$('#select_database option:selected').val();


seq_field = seq_field.replace(/\s/gm, '');

var error_text=validation(seq_field, num_outputs, cut_off, k_choice, random_from_best, region, selectedText);

if (error_text.length != 0){

$('#errors_area').css({'display':'block'});
$('#errors_area').html(error_text);
}

else {



$('#errors_area').html('');
$('#errors_area').css({'display':'none'});

    


  
  document.getElementById("num_outputs").readOnly = true;
  document.getElementById("seq").readOnly = true;
  document.getElementById("cut_off").readOnly = true;
  document.getElementById("k_choice").readOnly = true;
  document.getElementById("random_from_best").readOnly = true;
  document.getElementById("region").readOnly = true;
  document.getElementById("spoil").disabled = true;

    $('#loading-indicator').show();

    $.ajax({
        method: "POST",
        url: "spoil",
        data: { seq: seq_field, select: selectedText, num_outputs: num_outputs, cut_off: cut_off, k_choice: k_choice, random_from_best: random_from_best, region: region, csrfmiddlewaretoken: csrf_token },
		success:function(data) {
			processSpoil(data); 
		}

   })
}
}

function clickTestSpoil() {


    var database_name=$('#select_test_sequence option:selected').val();
    
    var seq='';
    var cut_off=0;


    var fly='TACTCAGCTGCTGATGCTGCACATAACTATGCACATACATATGAATGTACATATGTACGTTCCGTTGGAAAGAGAGATCACAACGGAGCGCCCATTCGTTGTATTCACTCTCACGTATCACACTGAACCATTGGCGTTAGTCTCATTTAGGCTTAATTGCGTAAAATTCTGATATTAAAAACATATTCATTTTAAACTCT';
    var fantom='catcaaggggcacttgcaggccagtgccaagccaccctcgtaccccctcatcttcccctcccatgctcctgctcctcagtgtccaaagtccagaaggggctgaggtggcaggggactggcatgtcagcactgcttccaatgtgtgcacacctggctgggcagtgacagcaccctgctgggtcccaaccccactctgagatcagagcacagagccaggaggtgggagagaccaggcagcaggaagaggtgcctccaagcctgcaaggggcaaggggggcgttcccaggctccccaagagtc'    
    var vista='ACCGCCGCGGCTTTTTGCTCCGTGCCGCTCGTTTTTGTCCCCGCCGCCGCGGCTTTTTGACCCCGCCGCCGCAGCTTTTTCCCCCAGTCGCGGGTTTTCGCCCCCACCGCAGCGATTTTCTGCCCCCGCCGCCGAGGCTTTTTGCCCCCGCCGCCACTACTTTTTGCGGCTTTTTGCCCACGCCGCCGCGGCTTTTTCCCCCACCGCCCGAGCTTTTTGCCGCCGGAGCTATCAGCCCCCGCCGCCGTGGCTTTTTCCCCCGATGCCGCGGCGTTTTGCCCCCGCCTCCGCGGTTTTTTTGTCCCCGCCGCTGAGACTTTTTGCCGCCATAGCTTTTTACCCGCGCCGCCACGGCTTTTTGTGGTTTTTTTTGCCCCCACTCCCGCTGCTTTTTGCTCCTGCCACCGCGGCTTTTTGCCCCCGCCGCGGATTTTTACCCCCGCCGCGGAGGATTTTTCCCCTGGTGCTGCGGCTCTGAGGGCAGGAGCGGCAGACTCGGCTGCTAGCTCCACTGGCGTCCTGGCAAGGGCAGCGCCGAGGGGCGCTCCTGGTCCAGCTCTCCTGGCTCGGGGGTTCTTTGCCTAGGCGCCGGCGCCCCGGGCTCCCTGCCTCGGCCTCTGTGGCCTGCATAGAGCGGCGCTGCGCGCAGAGGCGATGGGAGAGAAGAAGGAGGGTGGTGGCGGGGGTGATGCGGCATTAGCGGAAGGTGGCGCAGGGGCCGCGGGCAGCTCCAGAAGCTCATTGGCATCTTCATTGGCAGCCTTCGCTGGCTGGGCACCAAGTGCGCTGTGTCGAACGACCTCACCCAGCAGAAGATACCGACCCTGGAGGTAAGGGGTTCGGGGACCCGGGCTGGGCTCCAGGAGGAGCTCAGACACCTCCCTCGGGGCCCCAGTTCACTCCTGGCCCAGTTGCATCCTTGAGCCCGCATTGCGCCCTTGGAGTCTTCCCCTCCCTCCTGCATTCGCTGATGCGGCAGCAGGAGGACCCGGGACCAGCCCTCACCTTGAGCGCGATTTGTGGGGCGGGTGCGTGGTGGGAACTGGGATGAAGGATCCAGGGTCCTGTGGGGGGGGGTGGTGGGCTGTGCGCGGACATCCCCTTCCACCCTGAATTTCcatctggtccagccctctcatcttgtaggtgaggaaaccgaaggcctgaggaagaactgacttgccAGGAACCCCTGTTAAGGAGAATTATCAAAGTGTGGTTATTAAAGGAGAACTGAGATGGGAGTCAGACCTGGAGGCCCACACTCTTGGTTAAGACATTATACCACCTTGAGTCTGGCCTGTTTACTGAGGGTGAGCCACTCCATCCTTGTCTGATTGTGGGGTCTTGACCTCAAGGGGTTTCCTGCAGGAAGAAGCAAATGGGTTTGCTTTCCTAGCTCTGTCCAGTATCTTAGGGACCCTGAGGACTGAAGAGATTCTTGTAGAGCCATCTGGTGTATGTCATGGGTGGGCCTTTTTTGAATGTCAGTCTGCCCAT';


    if (database_name=='fly') {
    
    seq=fly;
    cut_off=0.63;
    }
    else if (database_name=='fantom') {
    seq=fantom;
    cut_off=0.10;
    }
    else if (database_name=='vista') {
    seq=vista;
    cut_off=0.20;
    }
   
    $("#seq").val(seq);
    document.getElementById("cut_off").value = cut_off;
    document.getElementById("k_choice").value = 10;       
    document.getElementById("random_from_best").value = 2;


}


function processSpoil(data)
{

  document.getElementById("num_outputs").readOnly = false;
  document.getElementById("seq").readOnly = false;
  document.getElementById("cut_off").readOnly = false;
  document.getElementById("k_choice").readOnly = false;
  document.getElementById("random_from_best").readOnly = false;
  document.getElementById("region").readOnly = false;
  document.getElementById("spoil").disabled = false;

  var obj = data;
  var text='';



  for (i = 0; i < obj.best_s.length; i++) {

    var num = i+1;
    text += "<div class=\"col-lg-12\"><hr></div></div>";
    text += "<div class=\"row\">";

    text += "<div class=\"col-lg-6\"><h3>Sequence mutated: " + num + "</h3><br><div><pre>" + obj.best_s[i] + "</pre></div></div>";

    text += "<div class=\"col-lg-6\"><br><br><h4>Positions:</h4><div><pre>";
    text +=  obj.mutations[i];
    text += "</pre></div></div>"

    text += "<div class=\"col-lg-6\"><h4>Prediction value:</h4><table  class=\"table table-bordered gray\"><thead><tr><th>original sequence</th><th>mutated sequence</th></tr></thead><tbody><tr> <td>"+ obj.o_pred[i] + "</td><td>" + obj.n_pred[i]+ "</td></tbody></table></div>";

}


$('#loading-indicator').hide();

$('#content_my').html(text);

}



