function callScript(){
    var data = document.getElementById("search_txt").value;
    console.log(data);
    $.ajax({
                  type: "POST",
                  url: "/suggestor",
                  //data: JSON.stringify(input),
                  data: data,
                  //contentType: 'application/json; charset=UTF-8',
                  dataType: 'json',
                  success: function(data) {
                  },
                  error: function(xhr, type){
                  	console.log("Error msg");
                  }
            });
     }