var noteControllers = angular.module('noteControllers', []);

noteControllers.controller('ListController', function ($scope, Note) {
    $scope.order = 'title';
    $scope.notes = Note.buildNotes();
    console.log($scope.notes);

    $scope.delNote = function(id) {
        Note.delNote(id);
        $scope.notes = Note.buildNotes();
        this.$root.$eval();
    }

    $scope.edit = function(id) {
        window.location = "./index.html#/edit/" + id;
    }

    $scope.backupNotes = function() {
        localStorage.setItem('backup', JSON.stringify($scope.notes));
    }

    $scope.restoreNotes = function() {
        $scope.notes = JSON.parse(localStorage.getItem('backup'));
        for (var i = 0; i < $scope.notes.length; i++) {
            var note = $scope.notes[i];
            Note.saveNote(note);
        }
        this.$root.$eval();
    }
});

noteControllers.controller('EditController', function ($scope, $routeParams, Note) {
    if($routeParams.noteId) {
        $scope.note = Note.findNote($routeParams.noteId);
    } else {
        $scope.note = {title: "", body: ""};
    }

    document.getElementById("title").value = $scope.note.title;
    document.getElementById("body").value = $scope.note.body;

    $scope.cancel = function() {
        window.location = "./index.html";
    }

    $scope.save = function(form) {
        $scope.note.title = document.getElementById("title").value;
        $scope.note.body = document.getElementById("body").value;
        Note.saveNote($scope.note);
        window.location = "./index.html"
    }
});

noteControllers.controller('DetailsController', function ($scope, $routeParams, Note) {
    $scope.note = Note.findNote($routeParams.noteId);

    $scope.back = function() {
        window.location = "./index.html";
    }
});
