Go language  (https://golang.org)
=========

This role installs Go language. It has been tested on Linux Mint 18 but should work on most 
distributions. By default it installs Go 1.8.3 linux/amd64 


Requirements
------------

None


Role Variables
--------------

    golang_version: 1.8.3.linux-amd64
    golang_download_mirror: https://storage.googleapis.com/golang/
    golang_download_directory: /tmp
    golang_install_directory: /usr/local
    golang_install_user: "{{ ansible_user_id }}"

    # calculated
    golang_install_file: "go{{ golang_version }}.tar.gz"
    golang_download_url: "{{ golang_download_mirror }}{{ golang_install_file }}"


Dependencies
------------

None

Example 
-------

__Example playbook__


    - hosts: localhost
      connection: local
    
    roles:
      - henriklyngaard.golang     
      
License
-------

MIT

Change log
----------

* 1.0: Initial version
