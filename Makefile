#########################################
CXX = mpic++
SRC_DIR := src
BUILD_DIR := build
TARGET := bin/zika_ip
QUESO_DIR := /Users/rebeccam/build/queso

SRC_EXT := cpp
SOURCES := $(shell find $(SRC_DIR) -type f -name *.$(SRC_EXT))
OBJECTS := $(patsubst $(SRC_DIR)/%,$(BUILD_DIR)/%,$(SOURCES:.$(SRC_EXT)=.o))

DATA_DIR := gendata
DATA_TARGET := bin/zika_fp
DATA_SOURCES := $(shell find $(DATA_DIR) -type f -name *.$(SRC_EXT))
DATA_COMMON_SOURCES := src/model.cpp src/dynamics_info.cpp
DATA_OBJECTS := $(patsubst $(DATA_DIR)/%,$(BUILD_DIR)/%,$(DATA_SOURCES:.$(SRC_EXT)=.o)) $(patsubst $(SRC_DIR)/%,$(BUILD_DIR)/%,$(DATA_COMMON_SOURCES:.$(SRC_EXT)=.o))
# build/model.o build/dynamics_info.o

# CXXFLAGS += -O3 -g -Wall -c -std=c++0x
CXXFLAGS += -O3 -g -Wall -std=c++0x
LIBS := \
	-L$(QUESO_DIR)/lib -lqueso \
	-L/usr/local/opt/icu4c/lib -lboost_program_options \
	-L/usr/local/opt/openssl/lib -lgsl -lgslcblas \
#	-L$(BOOST_DIR)/lib -lboost_program_options \
#	-L$(GSL_DIR)/lib -lgsl -lgslcblas\
#	-L$(GRVY_DIR)/lib -lgrvy \
#	-L$(MPI_DIR)/lib \
#	-L$(HDF5_DIR)/lib -lhdf5 
INC_PATHS := \
	-I include\
	-I$(QUESO_DIR)/include \
#	-I$(BOOST_DIR)/include \
#	-I$(GSL_DIR)/include \
#	-I$(GRVY_DIR)/include \
#	-I$(HDF5_DIR)/include \
#	-I$(GLPK_DIR)/include \
#	-I$(MPI_DIR)/ \
#	-I$(EIGEN_DIR)/include \

default: all

.SUFFIXES: .o .cpp

all: $(TARGET)

$(TARGET): $(OBJECTS)
	@echo " Linking..."
	@echo " $(CXX) $^ -o $(TARGET) $(LIBS)"; $(CXX) $^ -o $(TARGET) $(LIBS)
# zika-ip: glv.o compute.o dynamics_info.o likelihood.o model.o qoi.o 
# 	$(CXX) glv.o \
# 	       compute.o \
# 	       dynamics_info.o \
# 	       likelihood.o \
# 	       model.o \
# 	       qoi.o \
# 	       -o glv $(LIBS)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.$(SRC_EXT)
	@mkdir -p $(BUILD_DIR)
	@echo " $(CXX) $(CXXFLAGS) $(INC_PATHS) -c -o $@ $<"; $(CXX) $(CXXFLAGS) $(INC_PATHS) -c -o $@ $<

$(BUILD_DIR)/%.o: $(DATA_DIR)/%.$(SRC_EXT)
	@mkdir -p $(BUILD_DIR)
	@echo " $(CXX) $(CXXFLAGS) $(INC_PATHS) -c -o $@ $<"; $(CXX) $(CXXFLAGS) $(INC_PATHS) -c -o $@ $<

clean:
	@echo " Cleaning..."
	@echo " $(RM) -r $(BUILD_DIR)/* $(TARGET) bin/gen_data"; $(RM) -r $(BUILD_DIR)/* $(TARGET) bin/gen_data

# $(TARGET_DATA): $(OBJECTS_DATA)
# 	@echo " Linking..."
# 	@echo " $(CXX) $^ -o $(TARGET_DATA) $(LIBS)"; $(CXX) $^ -o $(TARGET_DATA) $(LIBS)
#
# test: $(TEST_OBJECTS) $(OBJECTS) $(DATA_OBJECTS)
# 	@echo " $(SOURCES) "
# 	$(CXX) $(CXXFLAGS) $^ $(INC_PATHS) $(LIBS) -o bin/test

gen_data: $(DATA_OBJECTS)
	@echo " $(SOURCES) "
	$(CXX) $(CXXFLAGS) $^ $(INC_PATHS) $(LIBS) -o bin/gen_data

# clean:
# 	@echo " Cleaning..."
# 	rm -f *~
# 	rm -f *.o
# 	rm -f glv_plus test_model gen_data

# test_model: test_model.o model.o dynamics_info.o
# 	$(CXX) test_model.o \
# 		     model.o \
# 				 dynamics_info.o \
# 	       -o test_model $(LIBS)

# test_chaperone: test_chaperone.o model.o reaction_info.o
# 	$(CXX) test_chaperone.o \
# 		     model.o \
# 				 reaction_info.o \
# 	       -o test_chaperone $(LIBS)

# test_thermo: test_thermo.o model.o reaction_info.o
# 	$(CXX) test_thermo.o \
# 		     model.o \
# 				 reaction_info.o \
# 	       -o test_thermo $(LIBS)

# gen_red: gen_reduced.o model_reduced.o dynamics_info.o
# 	$(CXX) gen_reduced.o \
# 		     model_reduced.o \
# 				 dynamics_info.o \
# 	       -o gen_red $(LIBS)

# %.o: %.c
# 	$(CXX) $(INC_PATHS) $(CXXFLAGS) $<

.PHONY: clean gen_data
