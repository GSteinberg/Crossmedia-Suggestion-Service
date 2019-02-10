function callScript(){
    var input = document.getElementById("search.txt").value;
    console.log(input);
    $.ajax({
                  type: "POST",
                  url: "/suggestor",
                  //data: JSON.stringify(input),
                  data : {
                    name : input,
                  },
                  type : 'POST',
                  //contentType: 'application/json; charset=UTF-8',
                  dataType: 'json',
                  success: function(data) {
                    console.log("sucess")
                  },
                  error: function(xhr, type){
                    console.log("Error msg");
                  }
            });
     }

