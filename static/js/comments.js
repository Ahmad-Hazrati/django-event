const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const editButtons = document.getElementsByClassName("btn-edit");
const deleteConfirm = document.getElementById("deleteConfirm");
const commentText = document.getElementsByTagName("textarea")[0];
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

// empty the comment text after post

commentText.value = "";

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}