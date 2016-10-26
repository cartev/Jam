var ReviewBox = React.createClass({
	render : function() { 
		return (
			<div>
				<form class="" id"post_review" action="post_review">
					<input type="text" name="Review">
					<input type="button" value="Publish">
				</form>
			</div>
		)
	}
});

function display_review_box(){
	ReactDOM.render(
		<ReviewBox/>
		document.getElementbyID('')
	);
}

function post_review(){
	var Review = {
		artist : '',
		album : '',
		reviewText : '',
		user : ''
	};

	// post call to API
}