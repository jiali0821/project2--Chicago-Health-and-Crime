var url = "/crime_area";

function buildPlot(){
   Plotly.d3.json(url, function(error, response){
   // console.log(response);

   var trace1 = {
       x: response.map( data => data.Community_Area_Name),
       y: response.map( data => data.Crime_Count),
       type: "bar"};
   
   var data = [trace1];
   
   var layout = {
       title: "Crime Number of Communities",
       xaxis: { title: "Community Name" },
       yaxis: { title: "Total Crime Number" }
       };
   
   Plotly.newPlot("bar-plot", data, layout);
   })
};

buildPlot();

var selector = document.getElementById('selDataset');
/////////////////////////////////////////////////////////// pie chart 
getOptions();

function getOptions() {
   // Grab a reference to the dropdown select element
   
   // Use the list of sample names to populate the select options
   Plotly.d3.json('crime_pie', function(error, response) {
    //    console.log('xxx', response);
       var area_names = []

       for (var i = 0; i < response.length;  i++) {
           // console.log("selector", selector)
           if (area_names.includes(response[i]["Community_Area_Name"])){
            // console.log(area_names)   
            continue

           }
           else{
           var currentOption = document.createElement('option');
           currentOption.text = response[i]["Community_Area_Name"];
           currentOption.value = response[i]["Community_Area_Name"];
           selector.appendChild(currentOption);
            
           area_names.push(response[i]["Community_Area_Name"])
        }
        
        }
   });
 };


// function select(X) {
//     return X.Community_Area_Name = ;
getData("Ashburn");
function getData(dataset) {
   Plotly.d3.json("/crime_pie", function(error, response){
   // console.log(response);

//    d3.select("#pie").remove();
 
     var final_results = response.filter(test => test.Community_Area_Name === dataset) ;
     
    //  console.log(final_results)

   var data = [{
   values: final_results.map(data => data.ID),
   labels: final_results.map(data => data.Primary_Type),
   type: "pie"
   }];
   var layout = { height: 600,width: 800};
   Plotly.newPlot("pie", data, layout);
   })
};


// function updatePlotly(newdata) {
//    var PIE = document.getElementById("pie");
//    Plotly.restyle(PIE, "values", [newdata]);
//  };