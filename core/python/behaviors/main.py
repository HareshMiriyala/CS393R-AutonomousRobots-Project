"""Blank behavior."""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from task import Task
import core
import memory

class Playing(Task):	
    """Main behavior task."""
    def run(self):
    	memory.speech.say('Hello, World!')
    	self.finish()

    pass
