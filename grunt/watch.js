module.exports = {
    python: {
        files: [
            'src/**/*.py'
        ],
        tasks: [
            'clean',
            'flake8'
        ]
    },
    js: {
        files: [
            'Gruntfile.js',
            'grunt/**/*.js'
        ],
        tasks: [
            'jshint'
        ]
    }
};
