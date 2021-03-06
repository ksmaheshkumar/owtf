#!/usr/bin/env python
"""

owtf is an OWASP+PTES-focused try to unite great tools and facilitate pen testing
Copyright (c) 2011, Abraham Aranguren <name.surname@gmail.com> Twitter: @7a_ http://7-a.org
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the copyright owner nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Declares the framework exceptions.

"""


class FrameworkException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class FrameworkAbortException(FrameworkException):
    pass


class PluginAbortException(FrameworkException):
    pass


class UnreachableTargetException(FrameworkException):
    pass

class UnresolvableTargetException(FrameworkException):
    pass

class DBIntegrityException(FrameworkException):
    pass


class InvalidTargetReference(FrameworkException):
    pass


class InvalidSessionReference(FrameworkException):
    pass


class InvalidTransactionReference(FrameworkException):
    pass


class InvalidParameterType(FrameworkException):
    pass


class InvalidWorkerReference(FrameworkException):
    pass


class InvalidErrorReference(FrameworkException):
    pass


class InvalidWorkReference(FrameworkException):
    pass


class InvalidConfigurationReference(FrameworkException):
    pass

class InvalidUrlReference(FrameworkException):
    pass

class InvalidActionReference(FrameworkException):
    pass

class InvalidMessageReference(FrameworkException):
    pass

class InvalidMappingReference(FrameworkException):
    pass
