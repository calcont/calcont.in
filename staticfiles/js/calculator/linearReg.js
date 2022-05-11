var tableArray = [];
function CreateTb(t){
    $('#tVal').empty();
    var entry = t.value;

    if(entry <51){
    document.getElementById("value-table").style.display = "block";
    for(var i = 0;i<entry;i++){
      var tble = `<tr>
                      <th scope="row">${i+1}</th>
                      <td><input type="number" class="form-control text-white  col-md-8" style="background-color:#1c2023;border: 2px solid #26313c; "   id="x${i+1}" required></td>
                      <td><input type="number" class="form-control  col-md-8 text-white" style="background-color:#1c2023;border: 2px solid #26313c; "   id="y${i+1}" required></td>
      
                    </tr>`;
                    $('#tVal').append(tble);
  }
  }
  }

  $('#viewResult').click(function (e) {
    
    document.getElementById("all-tables").style.display = "block";
    var x2="",y2="",xy ="";
  for(var i = 0;i<tableArray.length;i++){
  x2 += tableArray[i][0]*tableArray[i][0];
  y2 += tableArray[i][1]*tableArray[i][1];
  xy += tableArray[i][0]*tableArray[i][1];
  x2+="\r\n";
  y2+="\r\n";
  xy+="\r\n";
}
document.getElementById("xsq").innerHTML = x2;
document.getElementById("ysq").innerHTML = y2;
document.getElementById("xy").innerHTML = xy;
  e.preventDefault();
  });
  $(document).on('submit','#post-form',function(e){
  e.preventDefault();
tableArray = [];
  var entry = $('#No').val();
  var ans = document.getElementById("answers");
  ans.innerHTML = "";
  if(entry<51){
  for(var i = 0;i<entry;i++){
    var x = $('#x'+(i+1)).val();
    var y = $('#y'+(i+1)).val();
    tableArray.push([x,y]);
  }
  $.ajax({
          type:'POST',
          url:'/Calculator/Linear-regression-calculator/',
          data:{
              'tableArr[]':tableArray,
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          },
          encode:true,
          success:function(response){
            var GotRes=JSON.parse(response);
           
            ans.style.display = "block";
            for(var key in GotRes){
              if (GotRes.hasOwnProperty(key)) {
                ans.innerHTML += `<p class="my-2 ">${key} : ${GotRes[key]}</p>`;
            }
            }
            document.getElementById("viewResult").style.display = "block";
          },
         error:function(response){
          ans.innerHTML += `<p class="my-2 ">${key} : There is an unknown error!!}</p>`;;
          }

      })
    }
  });