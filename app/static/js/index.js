(()=>{
    const simple_chart_config = {
        chart: {
            container: "#tree-simple"
        },
        
        nodeStructure: {
            text: { name: "Parent node" },
            children: [
                {
                    text: { name: "First child" }
                },
                {
                    text: { name: "Second child" }
                }
            ]
        }
    };
    var my_chart = new Treant(simple_chart_config);
    // var chart = new Treant(simple_chart_config, function() { alert( 'Tree Loaded' ) }, $ );
})()