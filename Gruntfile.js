var path = require('path');

console.log('Grunt');

module.exports = function (grunt) {

    require('time-grunt')(grunt);

    require('load-grunt-config')(grunt);
    
    // require('load-grunt-config')(grunt, {
    //     configPath:  path.join(process.cwd(), 'grunt'),
    //     init: true,
    //     data: {
    //         test: false
    //     },
    //     loadGruntTasks: {
    //         pattern: 'grunt-*',
    //         config: require('./package.json'),
    //         scope: 'devDependencies'
    //     }
    // });

};
