module.exports = (grunt) ->
	grunt.initConfig
    pkg: grunt.file.readJSON 'package.json'

    watch:
      scripts:
        files: ['../../**/*.py']
        tasks: ['shell']
        options:
          spawn: false

    shell:
      deploy:
        options:
          stdout: true
          execOptions:
            timeout: 10000
        command: [
          '../kill.sh',
          '../deploy.sh',
          '../exec.sh'
          ].join('&&')


    grunt.loadNpmTasks 'grunt-shell'
    grunt.loadNpmTasks 'grunt-contrib-watch'

    grunt.registerTask 'default', ['watch']