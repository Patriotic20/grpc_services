# Makefile for gRPC Proto File Generation (Python)

# Variables
PROTO_DIR = protos
OUTPUT_DIR = generated

# Proto files
PROTO_FILES = $(wildcard $(PROTO_DIR)/*.proto)

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[0;33m
NC = \033[0m # No Color

.PHONY: all clean help proto

# Default target
all: proto

# Help command
help:
	@echo "Available commands:"
	@echo "  make proto         - Generate Python gRPC files"
	@echo "  make clean         - Remove generated files"
	@echo "  make help          - Show this help message"

# Generate Python files
proto:
	@echo "$(GREEN)Generating Python gRPC files...$(NC)"
	@for proto in $(PROTO_FILES); do \
		basename=$$(basename $$proto .proto); \
		echo "$(YELLOW)Processing $$proto...$(NC)"; \
		mkdir -p $(OUTPUT_DIR)/$$basename; \
		python -m grpc_tools.protoc \
			--python_out=$(OUTPUT_DIR)/$$basename \
			--grpc_python_out=$(OUTPUT_DIR)/$$basename \
			--pyi_out=$(OUTPUT_DIR)/$$basename \
			-I=$(PROTO_DIR) \
			$$proto; \
		echo "$(GREEN)✓ Generated in $(OUTPUT_DIR)/$$basename/$(NC)"; \
	done
	@echo "$(GREEN)✓ All Python gRPC files generated successfully!$(NC)"

# Clean generated files
clean:
	@echo "$(GREEN)Cleaning generated files...$(NC)"
	@rm -rf $(OUTPUT_DIR)
	@echo "$(GREEN)✓ Clean completed!$(NC)"