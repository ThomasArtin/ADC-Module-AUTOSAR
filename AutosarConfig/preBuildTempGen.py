import json

output = {
	"NB_OF_GROUPS" : {
		"view" : "Number Of Groups",
		"type" : "NUMBER"
	},
	"MAX_NB_OF_SAMPLES_PER_CHANNEL" : {
		"view" : "Number Of Samples per channel",
		"type" : "NUMBER"
	},
	"ADC_ENABLE_START_STOP_GROUP_API" : {
		"view" : "Enable START_GROUP API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_GRP_NOTIF_CAPABILITY" : {
		"view" : "Notify Capabilities",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_READ_GROUP_API" : {
		"view" : "Enable READ_GROUP API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_DEINIT_API" : {
		"view" : "Enable DEINIT API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_HW_TRIGGER_API" : {
		"view": "Enable HW_Trigger API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_GET_STREAM_API" : {
		"view": "Enable GET_STREAM API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_DEV_ERROR_DETECT" : {
		"view": "Enable Development Error API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_ENABLE_LIMIT_CHECK" : {
		"view": "Enable LIMIT_CHECK API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_ENABLE_QUEUING" : {
		"view": "Enable QUEUING API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_LOW_POWER_STATES_SUPPORT" : {
		"view": "Low Power Support",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_POWER_STAT_ASYNCH_TRANSITION_MODE" : {
		"view": "ASYNCH_TRANSITION_MODE",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_VERSION_INFO_API" : {
		"view": "Enable VERSION_INFO API",
		"type" : "BOOL",
		"values" : ["STD_ON", "STD_OFF"],
	},
	"ADC_PRIORITY_IMPLEMENTATION" : {
		"view": "Priority API",
		"type" : "SELECT",
		"options" : ["Hardware", "Software"],
		"values" : ["ADC_PRIORITY_HW", "ADC_PRIORITY_SW"],
	},
	"ADC_RESULT_ALIGNMENT" : {
		"view": "Enable Result Alignment",
		"type" : "SELECT",
		"options" : ["Right", "Left"],
		"values" : ["ADC_ALIGN_RIGHT", "ADC_ALIGN_LEFT"],
	},
}

a = json.dumps(output)
f = open("preCompile.gen", "w")
f.write(a)
f.close()