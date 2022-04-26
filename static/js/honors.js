
function prefillFields() {
    var trophies=JSON.parse(document.getElementById("editFormB").dataset.trophies_json);
    var trophy = document.getElementById('my_select');
    for(var k=0; k<trophies.length;k++){
        if(trophies[k][0]==trophy){
        document.getElementById('txtEdit').placeholder = trophies[k][1];
        document.getElementById('yearEdit').placeholder = trophies[k][2];
        }
    }
}
