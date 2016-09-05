/*var cells = Array.prototype.slice.call(document.getElementById("table").getElementsByTagName("td"));
for(var i in cells){
    console.log("My contents is \"" + cells[i].innerHTML + "\"");
}
*/

var p = {
	onload: function() {
		var rows = document.getElementById("table").rows;
		for(var i = 0, ceiling = rows.length; i < ceiling; i++) {
			rows[i].onclick = function() {
				alert(this.cells[0].innerHTML);
			}
      	}
	}
};

