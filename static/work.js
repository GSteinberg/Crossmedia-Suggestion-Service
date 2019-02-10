function callScript(){
    var input = document.getElementById("search_txt").value;
    console.log(input);
    $.ajax({
                  type: "POST",
                  url: "https://localhost:8080/templetes/src/suggestor.py",
                  data: input,
                  success: function(data) {
                      alert("success returned");
                  }
            });
     }