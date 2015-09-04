$(document).ready(function(){
		$('.tabTitle').click(function(){
			var id = $(this).attr("id");
			var content = id+"Content";
			$(".activeTab").removeClass("activeTab")
			$(this).addClass("activeTab");
			$(".tabDiv").each(function(){
				$(this).hide();

			});
			console.log(content);
			$("#"+content).show();
		});
	});